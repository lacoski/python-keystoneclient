# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from keystoneclient import auth
from keystoneclient import base
from keystoneclient import exceptions


class Project(base.Resource):
    """Represents an Identity project.

    Attributes:
        * id: a uuid that identifies the project
        * name: the name of the project
        * description: a description of the project
        * enabled: determines whether the project is enabled
        * parent_id: a uuid that identifies the specified project's parent
                     in hierarchy
        * parents: a list or a structured dict containing the parents of the
                   specified project in the hierarchy
        * subtree: a list or a structured dict containing the subtree of the
                   specified project in the hierarchy

    """


class Domain(base.Resource):
    """Represents an Identity domain.

    Attributes:
        * id: a uuid that identifies the domain
        * name: the name of the domain
        * description: a description of the domain
        * enabled: determines whether the domain is enabled

    """

    pass


class AuthManager(base.Manager):
    """Retrieve auth context specific information.

    The information returned by the auth routes is entirely dependant on the
    authentication information provided by the user.
    """

    _PROJECTS_URL = '/auth/projects'
    _DOMAINS_URL = '/auth/domains'

    def projects(self):
        """List projects that the specified token can be rescoped to.

        :returns: a list of projects.
        :rtype: list of :class:`keystoneclient.v3.projects.Project`

        """
        try:
            return self._list(self._PROJECTS_URL,
                              'projects',
                              obj_class=Project)
        except exceptions.EndpointNotFound:
            endpoint_filter = {'interface': auth.AUTH_INTERFACE}
            return self._list(self._PROJECTS_URL,
                              'projects',
                              obj_class=Project,
                              endpoint_filter=endpoint_filter)

    def domains(self):
        """List Domains that the specified token can be rescoped to.

        :returns: a list of domains.
        :rtype: list of :class:`keystoneclient.v3.domains.Domain`.

        """
        try:
            return self._list(self._DOMAINS_URL,
                              'domains',
                              obj_class=Domain)
        except exceptions.EndpointNotFound:
            endpoint_filter = {'interface': auth.AUTH_INTERFACE}
            return self._list(self._DOMAINS_URL,
                              'domains',
                              obj_class=Domain,
                              endpoint_filter=endpoint_filter)
