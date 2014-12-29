%define	snap	20121204
Summary:	General-purpose fonts released by Google as part of Android
Name:		fonts-TTF-Google-Droid
Version:	1.0.2
Release:	1.%{snap}.1
License:	Apache v2.0
Group:		Fonts
Source0:	google-droid-fonts-%{snap}.tar.xz
# Source0-md5:	d5768c1ce591d40375fd622ea68f11f9
Source1:	get-source.sh
Source10:	%{name}-sans.fontconfig
Source11:	%{name}-sans-mono.fontconfig
Source12:	%{name}-serif.fontconfig
Source13:	%{name}-kufi.fontconfig
URL:		http://android.git.kernel.org/?p=platform/frameworks/base.git;a=tree;f=data/fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
Requires:	fontconfig >= 1:2.10.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
The Droid typeface family was designed in the fall of 2006 by
Ascender's Steve Matteson, as a commission from Google to create a set
of system fonts for its Android platform. The goal was to provide
optimal quality and comfort on a mobile handset when rendered in
application menus, web browsers and for other screen text.

%prep
%setup -q -n google-droid-fonts-%{snap}
rm DroidSansFallbackFull*
rm DroidSansFallbackLegacy*
rm DroidNaskh-Regular-SystemUI*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ttffontsdir}
install -d $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail
install -d $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

cp -a *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}
cp -p %{SOURCE10} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/65-google-droid-sans.conf
cp -p %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/60-google-droid-sans-mono.conf
cp -p %{SOURCE12} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/65-google-droid-serif.conf
cp -p %{SOURCE13} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/65-google-droid-kufi.conf

ln -s %{_datadir}/fontconfig/conf.avail/65-google-droid-sans.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
ln -s %{_datadir}/fontconfig/conf.avail/60-google-droid-sans-mono.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
ln -s %{_datadir}/fontconfig/conf.avail/65-google-droid-serif.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
ln -s %{_datadir}/fontconfig/conf.avail/65-google-droid-kufi.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{_sysconfdir}/fonts/conf.d/65-google-droid-serif.conf
%{_sysconfdir}/fonts/conf.d/60-google-droid-sans-mono.conf
%{_sysconfdir}/fonts/conf.d/65-google-droid-sans.conf
%{_sysconfdir}/fonts/conf.d/65-google-droid-kufi.conf
%{_datadir}/fontconfig/conf.avail/65-google-droid-serif.conf
%{_datadir}/fontconfig/conf.avail/60-google-droid-sans-mono.conf
%{_datadir}/fontconfig/conf.avail/65-google-droid-sans.conf
%{_datadir}/fontconfig/conf.avail/65-google-droid-kufi.conf
%{_ttffontsdir}/Droid*.ttf
