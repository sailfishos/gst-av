Name:           gst-av
Version:        0.8.1
Release:        0.0
Summary:        GStreamer plug-in to access libav
License:        LGPL-2.1
Group:          Productivity/Multimedia/Video/Players
Url:            http://code.google.com/p/gst-av/
Source:         gst-av-%{version}.tar.gz
BuildRequires:  gstreamer-devel
BuildRequires:  libav-devel
BuildRequires:  pkgconfig(gstreamer-tag-0.10)
Requires:       gstreamer

%description
This package contains the GStreamer plug-in to access libav

%prep
%setup -q

%build
make

%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/%{_libdir}/gstreamer-0.10/libgstav.so
