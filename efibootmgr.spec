Summary:	EFI Boot Manager
Summary(pl.UTF-8):	Boot Manager dla EFI
Name:		efibootmgr
Version:	0.5.4
Release:	1
License:	GPL v2+
Group:		Base
Source0:	http://linux.dell.com/efibootmgr/permalink/%{name}-%{version}.tar.gz
# Source0-md5:	cfcf24752d6461b73f7ba964bbf73169
URL:		http://linux.dell.com/projects.shtml#efibootmgr
BuildRequires:	pciutils-devel
ExclusiveArch:	%{ix86} %{x8664} ia64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
efibootmgr displays and allows the user to edit the Intel Extensible
Firmware Interface (EFI) Boot Manager variables. Additional
information about EFI can be found at
<http://developer.intel.com/technology/efi/efi.htm>.

%description -l pl.UTF-8
efibootmgr wyświetla i pozwala modyfikować wartości Boot Managera
EFI (Extensible Firmware Interface) Intela. Dodatkowe informacje o EFI
można znaleźć pod adresem
<http://developer.intel.com/technology/efi/efi.htm>.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" \
%{__make} \
	CC="%{__cc}" \
	VPATH=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install src/efibootmgr/efibootmgr $RPM_BUILD_ROOT%{_sbindir}
install src/man/man8/efibootmgr.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README doc/{ChangeLog,TODO}
%attr(755,root,root) %{_sbindir}/efibootmgr
%{_mandir}/man8/efibootmgr.8*
