%define realname Catalyst-Plugin-Session-Store-FastMmap
%define abbrevname Catalyst-P-S-Store-FastMmap
%define name perl-%abbrevname
%define	modprefix Catalyst

%define version 0.02
%define release %mkrel 5

Summary:	FastMmap session storage backend
Name:		%name
Version:	%version
Release:	%release
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%realname/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%realname-%version.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Cache::FastMmap)
BuildRequires:	perl(Catalyst::Plugin::Session) >= 0.01
BuildRequires:	perl(Catalyst::Utils)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Path::Class)
Provides:	perl-%realname
Obsoletes:	perl-%realname
BuildArch:	noarch
Buildroot:	%_tmppath/%name-%{version}-%{release}-buildroot

%description
Catalyst::Plugin::Session::Store::FastMmap is a fast session storage plugin for
Catalyst that uses an mmap'ed file to act as a shared memory interprocess
cache. It is based on Cache::FastMmap.

%prep
%setup -q -n %realname-%version

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%perl_vendorlib/%{modprefix}
%_mandir/*/*

%clean
rm -rf %{buildroot}



