Summary:	A clone of the famous 8bit Atari game Robbo
Summary(pl.UTF-8):   Klon słynnej gry Robbo znanej z 8-bitowych Atari
Name:		gnurobbo
Version:	0.57
Release:	4
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/gnurobbo/%{name}-%{version}.tar.bz2
# Source0-md5:	575547d729528a13a0a56281311cc52e
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-stdlib.patch
URL:		http://gnurobbo.sourceforge.net/
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Robbo is very addictive logic game. You must help little robot to
get out of unfriendly planet, collecting parts of emergency capsule.

%description -l pl.UTF-8
GNU Robbo jest bardzo uzależniającą grą logiczną. Należy pomóc małemu
robotowi uciec z nieprzyjaznych planet zbierając części kapsuły
ratunkowej.

%prep
#%setup -q
# blegh, tarball contains icons in /... don't mess in %_builddir
%setup -q -c
%patch0 -p1

%build
cd %{name}-%{version}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
#cp config.h{,.in}
%{__autoheader}
%{__automake}
%configure \
	LDFLAGS="%{rpmldflags}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} -C %{name}-%{version} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}-%{version}/{AUTHORS,Bugs,ChangeLog,README,TODO}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
