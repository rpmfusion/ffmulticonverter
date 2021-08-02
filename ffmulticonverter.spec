Name:       ffmulticonverter
Version:    1.8.0
Release:    19%{?dist}
Summary:    GUI File Format Converter

License:    GPLv3+
URL:        https://sites.google.com/site/ffmulticonverter/home
Source0:    http://sourceforge.net/projects/ffmulticonv/files/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-setuptools
BuildRequires:  desktop-file-utils

Requires:   python3-qt5
Requires:   ImageMagick
Requires:   unoconv
Requires:   ffmpeg


%description
Graphical application which enables you to convert audio, video, image and
document files between all popular formats using ffmpeg, unoconv, and
ImageMagick.

Features:
 - Conversions for several file formats.
 - Very easy to use interface.
 - Access to common conversion options.
 - Audio/video ffmpeg-presets management.
 - Options for saving and naming files.
 - Recursive conversions

%prep
%autosetup


%build
%py3_build

%install
%py3_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%doc ChangeLog README.txt AUTHORS TRANSLATORS
%license COPYING
%{_bindir}/%{name}
%{python3_sitelib}/%{name}-%version-py%{python3_version}.egg-info
%{python3_sitelib}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.*

%changelog
* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.8.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Leigh Scott <leigh123linux@gmail.com> - 1.8.0-18
- Rebuild for python-3.10

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.8.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.8.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Leigh Scott <leigh123linux@gmail.com> - 1.8.0-15
- Rebuild for python-3.9

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.8.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 24 2019 Leigh Scott <leigh123linux@gmail.com> - 1.8.0-13
- Rebuild for python-3.8

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.8.0-10
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-8
- Rebuilt for Python 3.7

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Vasiliy N. Glazov <vascom2@gmail.com> 1.8.0-4
- Bump release for new python

* Sat Aug 13 2016 Vasiliy N. Glazov <vascom2@gmail.com> 1.8.0-3
- Correct license, requires and directory own

* Fri Aug 12 2016 Vasiliy N. Glazov <vascom2@gmail.com> 1.8.0-2
- Clean spec

* Tue Jul 19 2016 Vasiliy N. Glazov <vascom2@gmail.com> 1.8.0-1
- Update to 1.8.0

* Thu Jun 16 2016 Vasiliy N. Glazov <vascom2@gmail.com> 1.7.2-2
- Correct files handling
- Use pkgconfig in BR

* Fri Dec 18 2015 Vasiliy N. Glazov <vascom2@gmail.com> 1.7.2-1
- Update to 1.7.2

* Tue Jun 30 2015 Vasiliy N. Glazov <vascom2@gmail.com> 1.7.1-1
- Update to 1.7.1
- Use macros for python lib path

* Wed Mar 25 2015 Vasiliy N. Glazov <vascom2@gmail.com> 1.7.0-1
- Update to 1.7.0

* Wed Oct 08 2014 Vasiliy N. Glazov <vascom2@gmail.com> 1.6.0-2
- Bump rebuild for Fedora 21

* Mon Jan 13 2014 Vasiliy N. Glazov <vascom2@gmail.com> 1.6.0-1
- Update to 1.6.0

* Tue Jun 18 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.5.2-1
- Update to 1.5.2

* Fri May 24 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.5.1-1
- Initial release
