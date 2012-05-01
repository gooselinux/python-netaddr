%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

#====================================================================#

Name:           python-netaddr
Version:        0.7.5
Release:        3%{?dist}
Summary:        Pythonic manipulation of IPv4, IPv6, CIDR, EUI and MAC network addresses

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/drkjam/netaddr
Source0:        https://github.com/downloads/drkjam/netaddr/netaddr-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:      noarch
BuildRequires:  python-devel >= 2.4


%description
A pure Python network address representation and manipulation library.

netaddr provides a Pythonic way of working with :-

- IPv4 and IPv6 addresses and subnets (including CIDR notation)
- MAC (Media Access Control) addresses in multiple formats
- IEEE EUI-64, OUI and IAB identifiers
- a user friendly IP glob-style format

Included are routines for :-

- generating, sorting and summarizing IP addresses
- converting IP addresses and ranges between various different formats
- performing set based operations on groups of IP addresses and subnets
- arbitrary IP address range calculations and conversions
- querying IEEE OUI and IAB organisational information
- querying of IP standards related data from key IANA data sources

For examples please visit the example wiki pages :-

    http://code.google.com/p/netaddr/wiki/NetAddrExamples

Complete API documentation for the latest release is available online :-

    http://packages.python.org/netaddr/

For details on history changes and updates see the CHANGELOG :-

    http://code.google.com/p/netaddr/wiki/CHANGELOG


%prep
%setup -q -n netaddr-%{version}

# Make rpmlint happy, get rid of DOS line endings
%{__sed} -i 's/\r//' netaddr/*.py
%{__sed} -i 's/\r//' netaddr/ip/*.py
%{__sed} -i 's/\r//' netaddr/eui/*.idx

# Make rpmlint happy, rip out python shebang lines from most python
# modules
find netaddr -name "*.py" | \
  xargs %{__perl} -ni -e 'print unless /usr\/bin\/python|env\s+python/'

# Fix permissions on documentation files
chmod 0644 README AUTHORS CHANGELOG COPYRIGHT INSTALL LICENSE PKG-INFO


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%check
%{__python} netaddr/tests/__init__.py

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGELOG COPYRIGHT INSTALL LICENSE PKG-INFO
%doc README docs/api/
%{python_sitelib}/*
%{_bindir}/netaddr

%changelog
* Wed Jan 5 2010 Jakub Hrozek <jhrozek@redhat.com> - 0.7.5-3
- Fix permissions on documentation files
- Use correct upstream and source URLs

* Tue Jan 4 2010 Jakub Hrozek <jhrozek@redhat.com> - 0.7.5-2
- Rebase to 0.7.5 as that's what EPEL really has
- Bump release number to cleanly upgrade from EPEL

* Tue Jan 4 2010 Jakub Hrozek <jhrozek@redhat.com> - 0.7.4-2
- Rebase to 0.7.4
- Bump release number to cleanly upgrade from EPEL

* Wed Sep 30 2009 John Eckersberg <jeckersb@redhat.com> - 0.7.3-1
- New upstream release 0.7.3

* Fri Aug 21 2009 John Eckersberg <jeckersb@redhat.com> - 0.7.2-1
- New upstream release 0.7.2
- Updated Summary and Description with new values provided by upstream

* Mon Aug 17 2009 John Eckersberg <jeckersb@redhat.com> - 0.7.1-1
- New upstream release 0.7.1 fixes naming conflict with 'nash' by
  renaming the netaddr shell to 'netaddr'

* Wed Aug 12 2009 John Eckersberg <jeckersb@redhat.com> - 0.7-1
- Upstream release 0.7

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 John Eckersberg <jeckersb@redhat.com> - 0.6.3-2
- Minor tweaks to spec file aligning with latest Fedora packaging guidelines
- Enforce python 2.4 dependency as needed by netaddr >= 0.6.2
- Drop BR on python-setuptool as it is not imported in setup.py
- Drop BR on dos2unix use sed instead
- Align description with that of delivered PKG-INFO
- Rip out python shebangs
- Add %%check section to enable tests
- Thanks to Gareth Armstrong <gareth.armstrong@hp.com>

* Tue Jun 23 2009 John Eckersberg <jeckersb@redhat.com> - 0.6.3-1
- New upstream bugfix release

* Mon Apr 13 2009 John Eckersberg <jeckersb@redhat.com> - 0.6.2-1
- New upstream bugfix release

* Tue Apr 7 2009 John Eckersberg <jeckersb@redhat.com> - 0.6.1-1
- New upstream bugfix release

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 John Eckersberg <jeckersb@redhat.com> - 0.6-2
- Add BuildDepends on dos2unix to clean up some upstream sources

* Wed Feb 18 2009 John Eckersberg <jeckersb@redhat.com> - 0.6-1
- New upstream version

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.5.2-2
- Rebuild for Python 2.6

* Fri Oct 10 2008 John Eckersberg <jeckersb@redhat.com> - 0.5.2-1
- New upstream version, bug fixes for 0.5.1

* Tue Sep 23 2008 John Eckersberg <jeckersb@redhat.com> - 0.5.1-1
- New upstream version, bug fixes for 0.5

* Sun Sep 21 2008 John Eckersberg <jeckersb@redhat.com> - 0.5-1
- New upstream version

* Mon Aug 11 2008 John Eckersberg <jeckersb@redhat.com> - 0.4-1
- Initial packaging for Fedora

