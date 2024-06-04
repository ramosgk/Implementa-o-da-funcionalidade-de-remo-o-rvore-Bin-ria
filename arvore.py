class No:
    def começo(self, chave):
        self.esquerda = None
        self.direita = None
        self.valor = chave

class ArvoreBinariaBusca:
    def começo(self):
        self.raiz = None

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = No()
            self.raiz.começo(chave)
        else:
            self.inserir_no(self.raiz, chave)

    def inserir_no(self, no_atual, chave):
        if chave < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No()
                no_atual.esquerda.começo(chave)
            else:
                self.inserir_no(no_atual.esquerda, chave)
        elif chave > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No()
                no_atual.direita.começo(chave)
            else:
                self.inserir_no(no_atual.direita, chave)
        else:
            print("Valor já existe na árvore")

    def remover(self, chave):
        self.raiz = self.remover_no(self.raiz, chave)

    def remover_no(self, raiz, chave):
        if raiz is None:
            return raiz

        if chave < raiz.valor:
            raiz.esquerda = self.remover_no(raiz.esquerda, chave)
        elif chave > raiz.valor:
            raiz.direita = self.remover_no(raiz.direita, chave)
        else:
            if raiz.esquerda is None and raiz.direita is None:
                return None
            elif raiz.esquerda is None:
                return raiz.direita
            elif raiz.direita is None:
                return raiz.esquerda

            no_min_valor_maior = self.no_valor_minimo(raiz.direita)
            raiz.valor = no_min_valor_maior