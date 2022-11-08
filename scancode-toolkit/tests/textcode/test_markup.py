# -*- coding: utf-8 -*-
#
# Copyright (c) nexB Inc. and others. All rights reserved.
# ScanCode is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/nexB/scancode-toolkit for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#

import os

from commoncode.testcase import FileBasedTesting

from textcode import markup


class TestMarkup(FileBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

    def test_jsp_is_markup(self):
        test_file = self.get_test_loc(u'markup/java.jsp')
        assert markup.is_markup(test_file)

    def test_jsp_demarkup(self):
        test_file = self.get_test_loc(u'markup/java.jsp')
        result = list(markup.demarkup(test_file))
        expected = [
            u' version="1.0" encoding="ISO-8859-1"?>\r\n',
            u' <%@page  session="false" contentType="text/html; charset=ISO-8859-1" %>\r\n',
            u' <%@page  import="clime.messadmin.model.IServerInfo" %>\r\n',
            u' <%@taglib  prefix="core" uri="messadmin-core" %>\r\n',
            u' <%@taglib  prefix="format" uri="messadmin-fmt" %>\r\n',
            u' HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"--%>\r\n',
            u' HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"--%>\r\n',
            u' html \r\n',
            u'     PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\r\n',
            u'     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r\n',
            u' html \r\n',
            u'     PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"\r\n',
            u'     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"--%>\r\n',
            u' html PUBLIC "-//W3C//DTD XHTML 1.1//EN"\r\n',
            u' "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"--%>\r\n',
            u'\r\n',
            u' xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">\r\n',
            u' IServerInfo serverInfos = (IServerInfo) request.getAttribute("serverInfos");\r\n',
            u'   String webFilesRoot = (String) request.getAttribute("WebFilesRoot"); %>\r\n',
            u' value="${pageContext.request.servletPath}" var="submitUrl" scope="page"/--%> can use value="${pageContext.request.servletPath}" because this JSP is include()\'ed --%>\r\n',
            u' or use directly ${pageContext.request.requestURI} --%>\r\n',
            u" String submitUrl = request.getContextPath() + request.getServletPath(); /* Can use +request.getServletPath() because this JSP is include()'ed */ %>\r\n",
            u' \r\n',
            u'     http-equiv="content-type" content="text/html; charset=iso-8859-1 "/> \r\n',
            u'\t http-equiv="pragma" content="no-cache "/>  HTTP 1.0 -->\r\n',
            u'\t http-equiv="cache-control" content="no-cache,must-revalidate "/>  HTTP 1.1 -->\r\n',
            u'\t http-equiv="expires" content="0 "/>  0 is an invalid value and should be treated as \'now\' -->\r\n',
            u'\t http-equiv="content-language" content="en "/>  fr-FR --%>\r\n',
            u'\t name="author" content="Cedrik LIME "/> \r\n',
            u'\t name="copyright" content="copyright 2005-2006 Cedrik LIME "/> \r\n',
            u'\t name="robots" content="noindex,nofollow,noarchive "/> \r\n',
            u'\t Server System Informations \r\n',
            u'\t rel="stylesheet" type="text/css"  =" MessAdmin.css "/> \r\n',
            u'\t type="text/css">\r\n',
            u'\t \r\n',
            u'\t type="text/javascript" src=" js/getElementsBySelector.js"> \r\n',
            u'\t type="text/javascript" src=" js/behavior.js"> \r\n',
            u'\t type="text/javascript" src=" js/MessAdmin.js"> \r\n',
            u'\t type="text/javascript">// \n',
            u'\t\tfunction reloadPage() {\r\n',
            u'\t\t\twindow.location.reload();\r\n',
            u'\t\t}\r\n',
            u'\t//]]>\r\n',
            u'\t \r\n',
            u' \r\n',
            u' \r\n',
            u'\r\n',
            u' \n',
            u' border="0" cellspacing="0" cellpadding="0" width="100%">\r\n',
            u' \r\n',
            u' align="right" class="topheading" width="44"> alt="Indus Logo" border="0" height="39" width="44" src=" /MessAdmin/images/logo.gif">  class="topheading">Indus Application Management Console \r\n',
            u' \r\n',
            u' \r\n',
            u' \r\n',
            u' \r\n',
            u' border="0" cellspacing="0" cellpadding="0">\r\n',
            u' \r\n',
            u' class="backtab"> class="tabs"  ="http://localhost:8083/serverbydomain?querynames=*ias50%3A*">Server view  \r\n',
            u' width="2">  class="backtab"> class="tabs"  ="http://localhost:8083/empty?template=emptymbean">MBean view   width="2"> \r\n',
            u' class="backtab"> class="tabs"  ="http://localhost:8083/mbean?objectname=JMImplementation%3Atype%3DMBeanServerDelegate&template=about">About  \r\n',
            u' width="2">  class="fronttab"> class="tabs"  ="http://localhost:8888/ias50/MessAdmin">Session Admin  \r\n',
            u' \r\n',
            u' \r\n',
            u'------------------------>\r\n',
            u'\r\n',
            u' <jsp:include  page="header.jsp "/> \r\n',
            u'\r\n',
            u' border="0" cellspacing="0" cellpadding="0" width="100%">\r\n',
            u' \r\n',
            u'   class="darker"> \r\n',
            u' \r\n',
            u' \r\n',
            u'   class="lighter">\r\n',
            u'   id="menu" style="font-size: small;">\r\n',
            u'  [\r\n',
            u'  Server Informations\r\n',
            u'  |\r\n',
            u'    =" ?action=webAppsList">Web Applications list \r\n',
            u'  ]\r\n',
            u'   \r\n',
            u'   \r\n',
            u' \r\n',
            u' \r\n',
            u' \r\n',
            u'\r\n',
            u' \r\n',
            u'\t <legend> Server Information </legend> \r\n',
            u' style="text-align: left;" border="0">\r\n',
            u'\t \r\n',
            u'\t\t Server name \r\n',
            u'\t\t title=\'Working directory:  serverInfos.getSystemProperties().get("user.dir") %>\'> getServletConfig().getServletContext().getServerInfo() %> \r\n',
            u'\t\t Servlet version \r\n',
            u'\t\t  getServletConfig().getServletContext().getMajorVersion() %>. getServletConfig().getServletContext().getMinorVersion() %> \r\n',
            u'\t \r\n',
            u'\t \r\n',
            u'\t\t Temp file directory \r\n',
            u'\t\t  value=\' serverInfos.getSystemProperties().get("java.io.tmpdir") %> \'/>  \r\n',
            u'\t\t Running as \r\n',
            u'\t\t title=\'Home directory:  serverInfos.getSystemProperties().get("user.home") %>\'> value=\' serverInfos.getSystemProperties().get("user.name") %> \'/>  \r\n',
            u'\t \r\n',
            u'\t \r\n',
            u'\t\t Startup date \r\n',
            u'\t\t  value=" serverInfos.getStartupTime() %>" type="both" pattern="yyyy-MM-dd HH:mm:ss "/>  \r\n',
            u'\t\t colspan="2"> \r\n',
            u'\t \r\n',
            u' \r\n',
            u' \r\n',
            u'\r\n',
            u' \r\n',
            u'\t <legend> CPU and Memory </legend> \r\n',
            u' style="text-align: left;" border="0">\r\n',
            u' test=" serverInfos.getCpuCount() >= 0 %>">\r\n',
            u'\t \r\n',
            u'\t\t title="maximum number of processors available to the Java virtual machine">Number of CPUs \r\n',
            u'\t\t align="center"> value=" serverInfos.getCpuCount() %>" type="number "/>  \r\n',
            u'\t \r\n',
            u' \r\n',
            u'\t \r\n',
            u'\t\t title="amount of free memory in the system">Free Memory \r\n',
            u'\t\t class="number"> value=" serverInfos.getFreeMemory() %>" type="bytes "/>  \r\n',
            u'\t \r\n',
            u'\t \r\n',
            u'\t\t title="total amount of memory in the Java Virtual Machine">Total Memory \r\n',
            u'\t\t class="number"> value=" serverInfos.getTotalMemory() %>" type="bytes "/>  \r\n',
            u'\t \r\n',
            u' test=" serverInfos.getMaxMemory() >= 0 %>">\r\n',
            u'\t \r\n',
            u'\t\t title="maximum amount of memory that the Java virtual machine will attempt to use">Max Memory \r\n',
            u'\t\t class="number"> value=" serverInfos.getMaxMemory() %>" type="bytes "/>  \r\n',
            u'\t \r\n',
            u' \r\n',
            u' \r\n',
            u' \r\n',
            u'\r\n',
            u' \r\n',
            u'\t <legend> VM Info </legend> \r\n',
            u' extracted properties from System.getProperties() (see JavaDoc) -->\r\n',
            u' style="text-align: left;" border="0">\r\n',
            u'\t VM Info \r\n',
            u'\t \r\n',
            u'\t\t Java VM \r\n',
            u'\t\t \r\n',
            u'\t\t\t value=\' serverInfos.getSystemProperties().get("java.vm.vendor") %> \'/> \r\n',
            u'\t\t\t value=\' serverInfos.getSystemProperties().get("java.vm.name") %> \'/> \r\n',
            u'\t\t\t value=\' serverInfos.getSystemProperties().get("java.vm.version") %> \'/> \r\n',
            u'\t\t \r\n',
            u'\t \r\n',
            u'\t \r\n',
            u'\t\t Java RE \r\n',
            u'\t\t \r\n',
            u'\t\t\t  =" serverInfos.getSystemProperties().get("java.vendor.url") %>"> value=\' serverInfos.getSystemProperties().get("java.vendor") %> \'/>  \r\n',
            u'\t\t\t value=\' serverInfos.getSystemProperties().get("java.version") %> \'/>  @  value=\' serverInfos.getSystemProperties().get("java.home") %> \'/> \r\n',
            u'\t\t \r\n',
            u'\t \r\n',
            u'\t \r\n',
            u'\t\t Platform \r\n',
            u'\t\t \r\n',
            u'\t\t\t value=\' serverInfos.getSystemProperties().get("os.name") %> \'/> / value=\' serverInfos.getSystemProperties().get("os.arch") %> \'/> \r\n',
            u'\t\t\t value=\' serverInfos.getSystemProperties().get("os.version") %> \'/> \r\n',
            u'\t\t \r\n',
            u'\t \r\n',
            u' \r\n',
            u' \r\n',
            u'\r\n',
            u' style="text-align: center;"> type="button" onclick="window.location.reload()">Refresh  \r\n',
            u'\r\n',
            u' class="error"> value=\' request.getAttribute("error") %> \'/>  \r\n',
            u' class="message"> value=\' request.getAttribute("message") %> \'/>  \r\n',
            u'\r\n',
            u' id="extraServerAttributes">\r\n',
            u' items=" serverInfos.getServerSpecificData() %>" var="serverSpecificData" varStatus="status">\r\n',
            u' java.util.Map.Entry serverSpecificData = (java.util.Map.Entry) pageContext.getAttribute("serverSpecificData"); %>\r\n',
            u'\t \r\n',
            u'\t\t <legend  > serverSpecificData.getKey() %> </legend> \r\n',
            u'\t\t serverSpecificData.getValue() %>\r\n',
            u'\t \r\n',
            u' \r\n',
            u' \r\n',
            u'\r\n',
            u' <jsp:include  page="footer.jsp "/> \r\n',
            u'\r\n',
            u' \r\n',
            u' '
        ]
        assert result == expected
