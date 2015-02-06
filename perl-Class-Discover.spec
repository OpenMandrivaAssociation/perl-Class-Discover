%define upstream_name    Class-Discover
%define upstream_version 1.000003

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Detect MooseX::Declare's 'class' keyword in files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MM_Unix)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(File::Find::Rule::Perl)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(PPI)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This class is designed primarily for tools that whish to populate the
'provides' field of META.{yml,json} files so that the CPAN indexer will pay
attention to the existance of your classes, rather than blithely ignoring
them.

The version parsing is basically the same as what M::I's '->version_form'
does, so should hopefully work as well as it does.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.0.3-2mdv2011.0
+ Revision: 658741
- rebuild for updated spec-helper

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 553072
- update to 1.000003

* Tue Aug 18 2009 Jérôme Quelin <jquelin@mandriva.org> 1.0.1-1mdv2010.0
+ Revision: 417644
- import perl-Class-Discover


* Tue Aug 18 2009 cpan2dist 1.000001-1mdv
- initial mdv release, generated with cpan2dist
