Summary:	A clone of the famous 8bit Atari game Robbo
Summary(pl):	Klon s³ynnej gry Robbo znanej z 8-bitowych Atari
Name:		gnurobbo
Version:	0.54
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://gnurobbo.sourceforge.net/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://xpired.temnet.org/
BuildRequires:	SDL-devel
BuildRequires:	SDL_ttf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Help the robot called Robbo find all screws he needs :-)

%prep
%setup -q

# workaround for bad timestamps on files in source tarball
find . -type f | xargs touch

%build
%configure \
	CPPFLAGS="-I/usr/X11R6/include" \
	LDFLAGS="%{rpmldflags} -L/usr/X11R6/lib"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Bugs ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
