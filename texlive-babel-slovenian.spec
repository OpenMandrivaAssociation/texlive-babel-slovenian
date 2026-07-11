%global tl_name babel-slovenian
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2p
Release:	%{tl_revision}.1
Summary:	Babel support for typesetting Slovenian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/slovenian
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-slovenian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-slovenian.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-slovenian.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the language definition file for support of
Slovenian in babel. Several shortcuts are defined, as well as
translations to Slovenian of standard "LaTeX names".

