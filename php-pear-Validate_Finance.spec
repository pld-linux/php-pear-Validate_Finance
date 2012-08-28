%define		status		alpha
%define		pearname	Validate_Finance
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Validation class for finance
Summary(pl.UTF-8):	%{pearname} - Klasa sprawdzająca poprawność dla finansów
Name:		php-pear-%{pearname}
Version:	0.5.6
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	4abf83a0bdb2d5cf3f0b54996617c33a
URL:		http://pear.php.net/package/Validate_Finance/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(core) >= 4.2.0
Requires:	php-pear >= 4:1.0-4
Requires:	php-pear-PEAR-core >= 1:1.4.0
Requires:	php-pear-Validate >= 0.5.0
Obsoletes:	php-pear-Validate_Finance-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package to validate Finance data. It includes:
- IBAN

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności danych finansowych. Dotyczy to:
- numerów IBAN

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/*.php
%{php_pear_dir}/Validate/Finance/*.php
