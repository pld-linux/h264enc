Summary:	Shell script for encoding DVDs or video files to the H.264 format
Summary(pl.UTF-8):	Skrypt powłoki do konwersji płyt DVD i plików wideo do formatu H.264
Name:		h264enc
Version:	8.7.0
Release:	0.1
License:	GPL v2
Group:		Applications/Console
Source0:	http://dl.sourceforge.net/h264enc/%{name}-%{version}.tar.gz
# Source0-md5:	5533ab63f879252feb574b56dc811c0a
URL:		http://sourceforge.net/projects/h264enc/
Requires:	bash
Requires:	mencoder
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Advanced shell script for encoding DVDs or video files to the H.264
format using the encoding utility MEncoder from MPlayer. Supports all
the useful options an end-user would need to make a successful encode.
The script is a CLI front end to MEncoder.

%description -l pl.UTF-8
Zaawansowany skrypt powłoki wykorzystujący mencodera do kodowania płyt
DVD i plików wideo do formatu H.264. Wspiera wszystkie użyteczne
opcje, których może potrzebować użytkownik końcowy. Skrypt jest
front-endem CLI do mencodera.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1

install h264enc $RPM_BUILD_ROOT%{_bindir}
install man/h264enc.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/AUTHORS doc/ChangeLog doc/README.encoding doc/README.h264enc doc/README.matrices doc/preset.cfg
%doc matrices/*
%attr(755,root,root) %{_bindir}/h264enc
%{_mandir}/man1/h264enc.1*