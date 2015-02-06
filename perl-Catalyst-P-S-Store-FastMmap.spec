%define upstream_name    Catalyst-Plugin-Session-Store-FastMmap
%define abbrev_name      Catalyst-P-S-Store-FastMmap
%define upstream_version 0.16

Name:		perl-%{abbrev_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	FastMmap session storage backend
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Catalyst/Catalyst-Plugin-Session-Store-FastMmap-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
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
Requires:	perl(MooseX::Emulate::Class::Accessor::Fast)
%rename	perl-%{upstream_name}


%description
Catalyst::Plugin::Session::Store::FastMmap is a fast session storage plugin for
Catalyst that uses an mmap'ed file to act as a shared memory interprocess
cache. It is based on Cache::FastMmap.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL installdirs=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.130.0-2mdv2011.0
+ Revision: 654823
- rebuild

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2011.0
+ Revision: 461723
- update to 0.13

* Wed Jul 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 396341
- adding missing buildrequires:
- update to 0.11
- using %%perl_convert_version

* Tue Jun 02 2009 Olivier Thauvin <nanardon@mandriva.org> 0.10-1mdv2010.0
+ Revision: 382086
- buildrequires
- 0.10

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.02-7mdv2009.0
+ Revision: 255583
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.02-5mdv2008.1
+ Revision: 136678
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-5mdv2008.0
+ Revision: 85940
- rebuild


* Tue Aug 08 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-08 03:53:48 (54354)
- Rebuild, spec file cleanup

* Tue Aug 08 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-08 03:50:03 (54352)
- import perl-Catalyst-P-S-Store-FastMmap-0.02-3mdk

* Wed May 17 2006 Scott Karns <scottk@mandriva.org> 0.02-3mdk
- Updated BuildRequires
- Added source URL

* Fri Apr 14 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.02-2mdk
- Abbreviate rpm name to fit in the 64 char limit

* Thu Jan 12 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.02-1mdk
- Initial MDV RPM



