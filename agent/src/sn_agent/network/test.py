from sn_agent.network.base import NetworkBase
from sn_agent.network.provider import Provider


class TestNetwork(NetworkBase):
    def join(self) -> bool:
        """
        Agent calls this the first time to connect to the network. An Private and Public key should be returned
        """
        raise NotImplementedError()

    def leave(self) -> bool:
        """
        Should this do something in the blockchain or just delete the public and private keys?
        """
        raise NotImplementedError()

    def status(self) -> bool:
        """
        Determine what the current network status is
        :return:
        """
        raise NotImplementedError()

    def get_ontology(self):
        """
        Asks for the latest ontology
        :return:
        """
        raise NotImplementedError()

    def advertise(self, agent_id: str, ontology_node_id) -> bool:
        """

        :param agent_id:
        :param ontology_node_id:
        :return:
        """
        raise NotImplementedError()

    def deadvertise(self, agent_id: str, ontology_node_id) -> bool:
        """

        :param agent_id:
        :param ontology_node_id:
        :return:
        """
        raise NotImplementedError()

    def find_providers(self, ontology_node_id) -> list:
        """
        Called by the UI as well as find_provider - should return a list that contains information about all the providers that have indicated that they can proved the designated service
        :param ontology_node_id:
        :return:
        """

        providers = []
        agent_id = 'testing'
        providers.append(Provider(self, agent_id, 'eced6a6f-1051-4209-92b9-fbb78f66eb0b'))
        providers.append(Provider(self, agent_id, '37589980-a62d-4850-9ba0-5f8aff490ace'))

        return providers

    def ask_agent_if_can_perform(self, agent_id, ontology_node_id) -> bool:
        """
        :param agent_id:
        :param ontology_node_id:
        :return:
        """

        return True

    def ask_agent_to_perform(self, agent_id, ontology_id, json_content) -> bool:
        """

        :return:
        """
        raise NotImplementedError()

    def ask_agent_for_their_providers(self, agent_id, ontology_node_id) -> list:
        """
        This is used for creating the tree of services behind a given ontology

        :param agent_id:
        :param ontology_node_id:
        :return:
        """
        raise NotImplementedError()

    def can_i_perform(self, ontology_node_id) -> bool:
        """
        This is a request coming from the network asking if I can actually do the service

        :param ontology_node_id:
        :return:
        """

    def perform(self, ontology_node_id, json_content) -> bool:
        """
        This will instruct the worker to do the task requested

        :param ontology_node_id:
        :param json_content:
        :return:
        """
