%define __python /usr/bin/python3

Summary: Ansible Automation Platform (AAP) package protector DNF plugin
Name: aap-protector
Version: 0.1
Release: 1%{?dist}
Group: System Environment/Base
License: GPLv3
URL: https://github.com/knumskull/aap-protector
Source0: aap-protector.py
Source1: aap-protector.conf
Source2: aap-protector.list

Source20: LICENSE
Source21: README.md

BuildArch: noarch

Requires: dnf


%description
AAP provides a DNF plugin that protects packages required by AAP
that are sensitive to upgrades.

%install
install -d -m755 %{buildroot}%{_sysconfdir}/dnf/plugins
install -d -m755 -p %{buildroot}%{_docdir}/%{name}
install -d -m755 %{buildroot}%{python_sitelib}/dnf-plugins/

install -m755 %{SOURCE0} %{buildroot}%{python_sitelib}/dnf-plugins/
install -m644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/dnf/plugins
install -m644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/dnf/plugins

install -m644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/dnf/plugins/aap-protector.list
install -m644 %{SOURCE20} %{buildroot}%{_docdir}/%{name}/
install -m644 %{SOURCE21} %{buildroot}%{_docdir}/%{name}/

%files
%{python_sitelib}/dnf-plugins/aap-protector.py*
%{python_sitelib}/dnf-plugins/__pycache__/aap-protector.*
%config(noreplace) %{_sysconfdir}/dnf/plugins/aap-protector.*

%doc %{_docdir}/*

%changelog
* Thu Dec 15 2022 Oliver Falk <oliver@linux-kernel.at> - 0.1
- Initial release
