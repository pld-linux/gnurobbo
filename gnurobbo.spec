Summary:	A clone of the famous 8bit Atari game Robbo
Summary(pl):	Klon s³ynnej gry Robbo znanej z 8-bitowych Atari
Name:		gnurobbo
Version:	0.57
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://telia.dl.sourceforge.net/sourceforge/gnurobbo/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://gnurobbo.sf.net/
BuildRequires:	SDL_ttf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
GNU Robbo is very addictive logic game. You must help
little robot to get out of unfriendly planet, collecting
parts of emergency capsule.

%description -l pl
GNU Robbo jest bardzo uzale¿niaj±c± gr± logiczn±. Nale¿y pomóc
ma³emu robotowi uciec z nieprzyjaznych planet zbieraj±c czê¶ci
kapsu³y ratunkowej.

%prep
#%setup -q
# blegh, tarball contains icons in /... don't mess in %_builddir
%setup -q -c

# workaround for bad timestamps on files in source tarball
#find . -type f | xargs touch

%build
cd %{name}-%{version}
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
cp config.h{,.in}
%{__automake}
%configure \
	CPPFLAGS="-I/usr/X11R6/include" \
	LDFLAGS="%{rpmldflags} -L/usr/X11R6/lib"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games,%{_pixmapsdir}}

cd %{name}-%{version}
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}-%{version}/{AUTHORS,Bugs,ChangeLog,README,TODO}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
