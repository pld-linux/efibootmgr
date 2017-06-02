Summary:	EFI Boot Manager
Summary(pl.UTF-8):	Boot Manager dla EFI
Name:		efibootmgr
Version:	15
Release:	1
License:	GPL v2+
Group:		Base
Source0:	https://github.com/rhinstaller/efibootmgr/releases/download/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	62597b082f27da940bf18f0ec8c5907b
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
%{__make} \
	CC="%{__cc}" \
	EFIDIR=pld \
	EXTRA_CFLAGS="%{rpmcflags} -I/usr/include/efivar" \
	VPATH=%{_libdir} \
	libdir=%{_libdir}

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
