Summary:	EFI Boot Manager
Summary(pl.UTF-8):	Boot Manager dla EFI
Name:		efibootmgr
Version:	14
Release:	1
License:	GPL v2+
Group:		Base
Source0:	https://github.com/rhinstaller/efibootmgr/releases/download/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	f74e87963c2c5cb1bf6d588675dbd9b4
URL:		https://github.com/rhinstaller/efibootmgr
BuildRequires:	efivar-devel >= 0.20
BuildRequires:	pciutils-devel
Requires:	efivar >= 0.20
ExclusiveArch:	%{ix86} %{x8664} ia64 x32
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
%setup -q -n %{name}-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	EXTRA_CFLAGS="%{rpmcflags} -I/usr/include/efivar" \
	VPATH=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install src/efibootmgr $RPM_BUILD_ROOT%{_sbindir}
install src/efibootdump $RPM_BUILD_ROOT%{_sbindir}
install src/efibootmgr.8 $RPM_BUILD_ROOT%{_mandir}/man8
install src/efibootdump.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md TODO
%attr(755,root,root) %{_sbindir}/efibootdump
%attr(755,root,root) %{_sbindir}/efibootmgr
%{_mandir}/man8/efibootdump.8*
%{_mandir}/man8/efibootmgr.8*
