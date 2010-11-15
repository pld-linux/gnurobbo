Summary:	A clone of the famous 8bit Atari game Robbo
Summary(pl.UTF-8):	Klon słynnej gry Robbo znanej z 8-bitowych Atari
Name:		gnurobbo
Version:	0.66
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/gnurobbo/%{name}-%{version}-source.tar.gz
# Source0-md5:	77fdf9a186a08c1f95b94bd35ebbc21c
Source1:	%{name}.desktop
Patch0:		%{name}-flags.patch
URL:		http://gnurobbo.sourceforge.net/
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Robbo is very addictive logic game. You must help little robot to
get out of unfriendly planet, collecting parts of emergency capsule.

%description -l pl.UTF-8
GNU Robbo jest bardzo uzależniającą grą logiczną. Należy pomóc małemu
robotowi uciec z nieprzyjaznych planet zbierając części kapsuły
ratunkowej.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	PACKAGE_DATA_DIR=%{_datadir}/%{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	PACKAGE_DATA_DIR=$RPM_BUILD_ROOT%{_datadir}/%{name} \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	DOCDIR=data

cp -r data/skins/tronic $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/
cp -r data/locales $RPM_BUILD_ROOT%{_datadir}/%{name}/

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install icon32.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Bugs ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
