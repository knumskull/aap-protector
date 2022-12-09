import configparser

import dnf
import dnf.exceptions
from dnfpluginscore import _, logger


class AnsibleAutomationPlatformProtector(dnf.Plugin):
    """ Protect packages to allow out-of-bound updates.
    """
    name = 'aap-protector'
    config_name = 'aap-protector'

    def __init__(self, base, cli) -> None:
        super().__init__(base, cli)
        self.base = base
        self.cli = cli

    def _get_package_list_file_url(self) -> str:
        """ Method to get path tp package list file from configuration file.
        """
        try:
            parser = self.read_config(self.base.conf)
        except Exception as err:
            raise dnf.exceptions.Error(_("Parsing file failed: {}").format(str(err)))

        if parser.has_section('main'):
            file_url = parser.get('main', 'package_list')
        else:
            raise dnf.exceptions.Error(_('Incorrect plugin configuration!'))
        return file_url

    def _load_package_list(self) -> set:
        """ Method to parse package list file """
        file_url = self._get_package_list_file_url()
        package_whitelist = set()
        try:
            with open(file_url, 'r', encoding='utf8') as list_file:
                for line in list_file.readlines():
                    if line.startswith('#') or line.strip() == '':
                        continue
                    package_whitelist.add(line.rstrip())
        except IOError as err:
            raise dnf.exceptions.Error(f'Unable to read AAP protector"s configuration: {err}')
        return package_whitelist

    def sack(self):
        excluded_pkgs_query = self._load_package_list()
        total = len(excluded_pkgs_query)
        logger.info(_('Reading AAP protector configuration'))
        self.base.sack.add_excludes(excluded_pkgs_query)

        logger.info(_(f'*** Excluded total: {total}'))
        if total:
            if total > 1:
                suffix = 's'
            else:
                suffix = ''
            logger.info(_('\n'
                            f'WARNING: Excluding {total} package{suffix} due to aap-protector. \n'
                            'Disable aap-protector plugin and follow documentation to upgrade AAP.'
                        ))
        else:
            logger.info(_('\n'
                            'Nothing excluded by aap-protector!\n'))
