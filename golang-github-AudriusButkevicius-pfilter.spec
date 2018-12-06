# https://github.com/AudriusButkevicius/pfilter
%global goipath github.com/AudriusButkevicius/pfilter
Version:        0.0.3

%gometa

Name:           golang-github-AudriusButkevicius-pfilter
Release:        6%{?dist}
Summary:        Simple Packet Filtering package written in Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE


%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.3-6
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0.0.3-5
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.0.3-4
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.0.3-1
- Update to version 0.0.3.

* Thu Nov 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.0.2-1
- Update to version 0.0.2.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.0.1-1
- Bump version to latest release (no code changes).

* Tue Mar 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.20170209.git09b3cfd
- First package for Fedora

