Name:           gaming-companion
Version:        1.0
Release:        1%{?dist}
Summary:        Supercharge ta Fedora avec gaming companion

License:        GPL
URL:            https://github.com/DXC-0/Gaming-Companion
Source0:        gaming-companion-1.0.tar.xz

BuildArch:      noarch
Requires:       python3

%description
Un assistant pour le gaming sous Fedora Workstation

%prep
%setup -q

%install
mkdir -p %{buildroot}/bin/gaming-companion
mkdir -p %{buildroot}/bin/gaming-companion/scripts
mkdir -p %{buildroot}/usr/share/applications
mkdir -p %{buildroot}/usr/share/pixmaps

cp app.py %{buildroot}/bin/gaming-companion/app.py
cp style.css %{buildroot}/bin/gaming-companion/style.css

cp scripts/codecs.sh %{buildroot}/bin/gaming-companion/scripts/codecs.sh
cp scripts/drivers.sh %{buildroot}/bin/gaming-companion/scripts/drivers.sh
cp scripts/gaming-plus.sh %{buildroot}/bin/gaming-companion/scripts/gaming-plus.sh
cp scripts/gaming.sh %{buildroot}/bin/gaming-companion/scripts/gaming.sh
cp scripts/overclocking.sh %{buildroot}/bin/gaming-companion/scripts/overclocking.sh
cp scripts/protoncachy.sh %{buildroot}/bin/gaming-companion/scripts/protoncachy.sh
cp scripts/protonge.sh %{buildroot}/bin/gaming-companion/scripts/protonge.sh
cp scripts/rpm-fusion.sh %{buildroot}/bin/gaming-companion/scripts/rpm-fusion.sh
cp scripts/update.sh %{buildroot}/bin/gaming-companion/scripts/update.sh
cp scripts/protonplus.sh %{buildroot}/bin/gaming-companion/scripts/protonplus.sh

cp gaming-companion.desktop %{buildroot}/usr/share/applications/
cp gc-icon.svg %{buildroot}/usr/share/pixmaps/gc-icon.svg
cp gc-icon.svg %{buildroot}/bin/gaming-companion/gc-icon.svg

chmod -R +x %{buildroot}/bin/gaming-companion

%files
/bin/gaming-companion/app.py
/bin/gaming-companion/scripts/codecs.sh
/bin/gaming-companion/scripts/drivers.sh
/bin/gaming-companion/scripts/gaming-plus.sh
/bin/gaming-companion/scripts/gaming.sh
/bin/gaming-companion/scripts/overclocking.sh
/bin/gaming-companion/scripts/protoncachy.sh
/bin/gaming-companion/scripts/protonge.sh
/bin/gaming-companion/scripts/rpm-fusion.sh
/bin/gaming-companion/scripts/update.sh
/bin/gaming-companion/scripts/protonplus.sh
/bin/gaming-companion/style.css
/bin/gaming-companion/gc-icon.svg
/usr/share/applications/gaming-companion.desktop
/usr/share/pixmaps/gc-icon.svg

%changelog
* Sat Oct 05 2025 <DXC-0> - 1.0