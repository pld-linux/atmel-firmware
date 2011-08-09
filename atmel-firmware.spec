%define		usb_version	0.1
Summary:	Firmware for Atmel at76c50x wireless network chips
Name:		atmel-firmware
Version:	1.3
Release:	1
License:	Redistributable, no modification permitted
Group:		Base/Kernel
URL:		http://at76c503a.berlios.de/
Source0:	http://www.thekelleys.org.uk/atmel/%{name}-%{version}.tar.gz
# Source0-md5:	415e16463151f2e953e9b3dceb7af45f
Source1:	http://download.berlios.de/at76c503a/at76_usb-firmware-%{usb_version}.tar.gz
# Source1-md5:	4577f3f9e596170ffaed49b7d20ca7f5
Provides:	at76_usb-firmware = %{usb_version}
Obsoletes:	at76_usb-firmware < %{usb_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The drivers for Atmel at76c50x wireless network chips in the Linux
2.6.x kernel but do not include the firmware.

This firmware needs to be loaded by the host on most cards using these
chips.

%prep
%setup -q -a1
mv at76_usb-firmware-%{usb_version}/COPYRIGHT COPYRIGHT-usb
mv at76_usb-firmware-%{usb_version}/README README-usb

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware
cp -p images/*.bin $RPM_BUILD_ROOT/lib/firmware
cp -p at76_usb-firmware-%{usb_version}/*.bin $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README COPYRIGHT-usb README-usb VERSION
/lib/firmware/*
