from abc import abstractmethod, ABC


class Drink(ABC):
    def __init__(self, input_name, input_proof, input_taste, input_recipe):
        self.__name = ...
        self.__proof = ...
        self.__taste = ...
        self.__recipe = ...
        self.__kind = ...  # 주종

    def __str__(self):
        return f"{self.__name} object"

    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def set_proof(self, proof):
        pass

    @abstractmethod
    def set_taste(self, taste):
        pass

    @abstractmethod
    def set_recipe(self, recipe):
        pass


class Cocktail(Drink):
    def __init__(self, input_name, input_proof, input_taste, input_recipe):
        super().__init__(input_name, input_proof, input_taste, input_recipe)
        self._color = ...  # 색상

    def set_name(self, input_name):
        self.__name = input_name

    def set_proof(self, input_proof):
        self.__proof = input_proof

    def set_taste(self, input_taste):
        self.__taste = input_taste

    def set_recipe(self, input_recipe):
        self.__recipe = input_recipe

    def set_color(self, input_color):
        self._color = input_color


# 가격 관련 내용
price_dict = {'Faust': 7000, 'soju': 1400}


if __name__ == "__main__":

    faust_recipe = {'technique': ['build', 'stir'],
                    'ingredients': {'overproof rum': 0.4, 'white rum': 0.4, 'Creme de Cassis': 0.2, 'ice': ..., 'unit': 'percent'},
                    'recipe_explanation': """1.오버프루프 럼을 1oz 넣어주세요.\n2. 화이트 럼을 1oz 넣어주세요.\n3. 크림 드 카시스를 1/2 넣어주세요.\n4. 바 스푼으로 저어 마무리합니다."""}

    # DB 관련 내용
    faust = Cocktail(input_name='Faust',
                     input_proof='sum(각 술의 도수 * 비율)',
                     input_taste='기본 레시피의 맛 설명 필요',
                     input_recipe=faust_recipe)

    soju = Drink(input_name='Soju',
                 input_proof='종류에 따라 다름.',
                 input_taste='기본 레시피의 맛 설명 필요',
                 input_recipe='제조법이 들어가야 함.')

import pandas as pd
# column name : 추출단어, 형태로 가정.
sample_dict = {'input_taste': ['달달한'], 'input_proof': ['32']}
sample_input_df = pd.DataFrame(sample_dict)

