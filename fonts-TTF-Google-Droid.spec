Summary:	General-purpose fonts released by Google as part of Android
Name:		fonts-TTF-Google-Droid
Version:	1.0.0.112
Release:	2
License:	Apache v2.0
Group:		Fonts
Source0:	google-droid.tar.gz
# Source0-md5:	db7948a148a065a59c48db27afa16b5d
Source1:	%{name}-sans.fontconfig
Source2:	%{name}-sans-mono.fontconfig
Source3:	%{name}-serif.fontconfig
URL:		http://android.git.kernel.org/?p=platform/frameworks/base.git;a=tree;f=data/fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
Requires:	fontconfig >= 1:2.10.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
The Droid typeface family was designed in the fall of 2006 by Ascender's
Steve Matteson, as a commission from Google to create a set of system fonts
for its Android platform. The goal was to provide optimal quality and comfort
on a mobile handset when rendered in application menus, web browsers and for
other screen text.

%prep
%setup -q -n base
rm -f Ahem.ttf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ttffontsdir}
install -d $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail
install -d $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

cp -a *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/65-droid-sans.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/60-droid-sans-mono.conf
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/59-droid-serif.conf
ln -s %{_datadir}/fontconfig/conf.avail/65-droid-sans.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
ln -s %{_datadir}/fontconfig/conf.avail/60-droid-sans-mono.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
ln -s %{_datadir}/fontconfig/conf.avail/59-droid-serif.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{_ttffontsdir}/Droid*.ttf
%{_datadir}/fontconfig/conf.avail/59-droid-serif.conf
%{_datadir}/fontconfig/conf.avail/60-droid-sans-mono.conf
%{_datadir}/fontconfig/conf.avail/65-droid-sans.conf
%{_sysconfdir}/fonts/conf.d/59-droid-serif.conf
%{_sysconfdir}/fonts/conf.d/60-droid-sans-mono.conf
%{_sysconfdir}/fonts/conf.d/65-droid-sans.conf
