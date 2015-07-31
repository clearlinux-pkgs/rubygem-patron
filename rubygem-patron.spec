#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-patron
Version  : 0.4.18
Release  : 3
URL      : https://rubygems.org/downloads/patron-0.4.18.gem
Source0  : https://rubygems.org/downloads/patron-0.4.18.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-patron-lib
BuildRequires : curl-dev
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-rake-compiler
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-simplecov

%description
= Ruby HTTP Client
== SYNOPSIS
Patron is a Ruby HTTP client library based on libcurl. It does not try to expose
the full "power" (read complexity) of libcurl but instead tries to provide a
sane API while taking advantage of libcurl under the hood.

%package lib
Summary: lib components for the rubygem-patron package.
Group: Libraries

%description lib
lib components for the rubygem-patron package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n patron-0.4.18
gem spec %{SOURCE0} -l --ruby > rubygem-patron.gemspec

%build
gem build rubygem-patron.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
patron-0.4.18.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/patron-0.4.18
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/patron-0.4.18.gem
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/ConnectionFailed/cdesc-ConnectionFailed.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Error/cdesc-Error.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/HostResolutionError/cdesc-HostResolutionError.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/PartialFileError/cdesc-PartialFileError.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/ProxyType/cdesc-ProxyType.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/action%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/action-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/action_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/auth_type%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/auth_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/buffer_size%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/buffer_size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/cdesc-Request.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/connect_timeout%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/connect_timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/credentials-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/file_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/headers%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/ignore_content_length-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/insecure-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/max_redirects%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/max_redirects-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/multipart-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/password-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/proxy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/proxy_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/timeout%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/upload_data%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/upload_data-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/url-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Request/username-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Response/body-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Response/cdesc-Response.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Response/charset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Response/charset_regex-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Response/convert_to_default_encoding%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Response/determine_charset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Response/headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Response/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Response/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Response/parse_headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Response/redirect_count-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Response/status-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Response/status_line-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Response/url-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/auth_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/base_url-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/buffer_size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/cdesc-Session.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/connect_timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/copy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/default_response_charset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/delete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/enable_cookie_session-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/enable_debug-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/escape-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/get-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/get_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/handle_cookies-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/handle_request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/head-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/ignore_content_length-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/insecure-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/interrupt-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/max_redirects-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/password-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/post-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/post_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/post_multipart-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/proxy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/proxy_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/put-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/put_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/reset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/set_debug_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/unescape-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/urldecode-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/urlencode-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Session/username-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/TimeoutError/cdesc-TimeoutError.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/TooManyRedirects/cdesc-TooManyRedirects.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/URLFormatError/cdesc-URLFormatError.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/UnsupportedProtocol/cdesc-UnsupportedProtocol.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Util/build_query_pairs_from_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Util/build_query_string_from_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/Util/cdesc-Util.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/cdesc-Patron.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/Patron/libcurl_version-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/patron-0.4.18/ri/ext/patron/page-Makefile.ri
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/patron-0.4.18/gem.build_complete
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/patron-0.4.18/gem_make.out
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/patron-0.4.18/mkmf.log
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/.autotest
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/.rspec
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/Gemfile.lock
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/README.txt
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/ext/patron/.RUBYARCHDIR.-.patron.time
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/ext/patron/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/ext/patron/Makefile
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/ext/patron/extconf.rb
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/ext/patron/membuffer.c
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/ext/patron/membuffer.h
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/ext/patron/membuffer.o
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/ext/patron/session_ext.c
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/ext/patron/session_ext.o
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/ext/patron/sglib.h
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/lib/patron.rb
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/lib/patron/error.rb
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/lib/patron/proxy_type.rb
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/lib/patron/request.rb
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/lib/patron/response.rb
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/lib/patron/session.rb
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/lib/patron/util.rb
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/lib/patron/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/patron.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/pic.png
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/script/console
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/script/test_server
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/spec/patron_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/spec/request_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/spec/response_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/spec/session_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/spec/support/test_server.rb
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/spec/util_spec.rb
/usr/lib64/ruby/gems/2.2.0/specifications/patron-0.4.18.gemspec

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/patron-0.4.18/patron/session_ext.so
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/ext/patron/session_ext.so
/usr/lib64/ruby/gems/2.2.0/gems/patron-0.4.18/lib/patron/session_ext.so
