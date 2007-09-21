/*
 * $Id$
 *
 * @Copyright@
 * @Copyright@
 * 
 * $Log$
 * Revision 1.2.2.1  2007/09/21 08:33:05  nadya
 * initial revision
 *
 */

function check_LocalHost(hostname)
{
	var retval = false;

	if (hostname.toLowerCase() == "localhost")
		retval = true; 

	return(retval);
}

function check_name(hostname)
{
	var retval = true;
	if (check_LocalHost(hostname) == true) 
		return(retval);

	if (check_fqdn(hostname) == false) {
		if (check_ipaddr(hostname) == false) {
			retval = false;
		}
	}

	return(retval);
}

function check_GFmetaserver(e)
{
	var doc = top.workarea.document;

	/*
	 * the user-input variable
	 */
	var GfarmMetaServer = doc.getElementsByName('Info_GfarmMetaServer')[0];

	return(check_name(GfarmMetaServer));
}

function check_GFagent(e)
{
	var doc = top.workarea.document;

	/*
	 * the user-input variable
	 */
	var GfarmAgent = doc.getElementsByName('Info_GfarmAgent')[0];

	return(check_name(GfarmAgent));
}

function check_GFfsnode(e)
{
	var doc = top.workarea.document;

	/*
	 * the user-input variable
	 */
	var GfarmFSNode = doc.getElementsByName('Info_GfarmFSNode')[0];
	if (GfarmFSNode.toLowerCase() == "none")
		return(true); 

	return(check_name(GfarmFSNode));
}

