Summary:	EFI Boot Manager
Summary(pl.UTF-8):	Boot Manager dla EFI
Name:		efibootmgr
Version:	16
Release:	1
License:	GPL v2+
Group:		Base
#Source0Download: https://github.com/rhboot/efibootmgr/releases
Source0:	https://github.com/rhinstaller/efibootmgr/releases/download/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	ab7cf46774fda951a0e8a40beb65a90e
URL:		https://github.com/rhinstaller/efibootmgr
BuildRequires:	efivar-devel >= 30
BuildRequires:	popt-devel
Requires:	efivar-libs >= 30
ExclusiveArch:	%{ix86} %{x8664} x32 %{arm} aarch64 ia64
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
	EFIDIR=pld \
	VPATH=%{_libdir} \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	EFIDIR=pld

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md TODO
%attr(755,root,root) %{_sbindir}/efibootdump
%attr(755,root,root) %{_sbindir}/efibootmgr
%{_mandir}/man8/efibootdump.8*
%{_mandir}/man8/efibootmgr.8*
