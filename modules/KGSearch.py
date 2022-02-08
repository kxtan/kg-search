import pandas as pd

class KGSearch(object):

    def __init__(self, triples_df:pd.DataFrame, 
        id_col="id", sub_col="subject",
        pred_col="predicate", obj_col="object") -> None:
        """[summary]

        Args:
            triples_df (pd.DataFrame): dataframe containing semantic triples of KG
        """

        self.process_triples(triples_df, id_col=id_col, sub_col=sub_col, 
            pred_col=pred_col, obj_col=obj_col)

        pass


    def process_triples(self, triples_df:pd.DataFrame,
        id_col="id", sub_col="subject",
        pred_col="predicate", obj_col="object") -> None:
        """[summary]

        Args:
            triples_df (pd.DataFrame): dataframe containing semantic triples of KG
            id_col (str, optional): id column name. Defaults to "id".
            sub_col (str, optional): subject column name. Defaults to "subject".
            pred_col (str, optional): predicate column name. Defaults to "predicate".
            obj_col (str, optional): object column name. Defaults to "object".

        """

        id_lst = triples_df[id_col].tolist()
        sub_lst = triples_df[sub_col].tolist()
        pred_lst = triples_df[pred_col].tolist()
        obj_lst = triples_df[obj_col].tolist()

        self.sub_dict = self._generate_dict(id_lst, sub_lst)
        self.pred_dict = self._generate_dict(id_lst, pred_lst)
        self.obj_dict = self._generate_dict(id_lst, obj_lst)


    def _generate_dict(self, id_lst:list, content_lst:list) -> dict:
        """Generate dictionary for hashing purposes

        Args:
            id_lst (list): list of id
            content_lst (list): list of content associated with the id

        Returns:
            dict: dictionary of content and its list of associated id
        """
        res_dict = {}

        for _id, content in zip(id_lst, content_lst):

            if content in res_dict:
                res_dict[content].append(_id)
            else:
                res_dict[content] = [_id]

        return res_dict


    def search_subject(self, query:str) -> list:
        """Return ID related to the query from subjects

        Args:
            query (str): the term to be searched

        Returns:
            list: list of related ids
        """
        if query in self.sub_dict:
            return self.sub_dict[query]
        return []


    def search_predicate(self, query:str) -> list:
        """Return ID related to the query from predicates

        Args:
            query (str): the term to be searched

        Returns:
            list: list of related ids
        """
        if query in self.pred_dict:
            return self.pred_dict[query]
        return []


    def search_object(self, query:str) -> list:
        """Return ID related to the query from objects

        Args:
            query (str): the term to be searched

        Returns:
            list: list of related ids
        """
        if query in self.obj_dict:
            return self.obj_dict[query]
        return []