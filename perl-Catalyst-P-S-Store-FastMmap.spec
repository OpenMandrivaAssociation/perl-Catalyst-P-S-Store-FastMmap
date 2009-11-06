%define upstream_name    Catalyst-Plugin-Session-Store-FastMmap
%define abbrev_name      Catalyst-P-S-Store-FastMmap
%define upstream_version 0.13

Name:		perl-%{abbrev_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	FastMmap session storage backend
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Cache::FastMmap)
BuildRequires:	perl(Catalyst::Plugin::Session) >= 0.01
BuildRequires:	perl(Catalyst::Utils)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Path::Class)
BuildRequires:  perl(MooseX::Emulate::Class::Accessor::Fast)
BuildRequires:  perl(namespace::clean)
BuildArch:	noarch
Buildroot:	%_tmppath/%name-%{version}-%{release}
Requires:   perl(MooseX::Emulate::Class::Accessor::Fast)
Provides:	perl-%{upstream_name}
Obsoletes:	perl-%{upstream_name}


%description
Catalyst::Plugin::Session::Store::FastMmap is a fast session storage plugin for
Catalyst that uses an mmap'ed file to act as a shared memory interprocess
cache. It is based on Cache::FastMmap.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL installdirs=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%perl_vendorlib/Catalyst
%_mandir/*/*

%clean
rm -rf %{buildroot}



