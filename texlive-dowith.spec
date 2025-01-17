Name:		texlive-dowith
Version:	38860
Release:	2
Summary:	Apply a command to a list of items
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/dowith
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dowith.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dowith.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dowith.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros for applying a command to all
elements of a list without separators, such as
'\DoWithAllIn{<cmd>}{<list-macro>}', and also for extending and
reducing macros storing such lists. Applications in mind
belonged to LaTeX, but the package should work with other
formats as well. Loop and list macros in other packages are
discussed. A further package, domore, is also provided, which
enhances the functionality of dowith.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/dowith/domore.sty
%{_texmfdistdir}/tex/generic/dowith/dowith.RLS
%{_texmfdistdir}/tex/generic/dowith/dowith.sty
%doc %{_texmfdistdir}/doc/generic/dowith/Announce.txt
%doc %{_texmfdistdir}/doc/generic/dowith/README
%doc %{_texmfdistdir}/doc/generic/dowith/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/generic/dowith/domore.pdf
%doc %{_texmfdistdir}/doc/generic/dowith/dowith.pdf
#- source
%doc %{_texmfdistdir}/source/generic/dowith/domore.tex
%doc %{_texmfdistdir}/source/generic/dowith/dowith.tex
%doc %{_texmfdistdir}/source/generic/dowith/fdatechk.tex
%doc %{_texmfdistdir}/source/generic/dowith/srcfiles.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
