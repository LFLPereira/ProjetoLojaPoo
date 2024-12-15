from Models.ControleEstoque import ControleEstoque

class Polymorph(ControleEstoque):
    def __init__(self, bd):
        super().__init__(bd)

    def logo(self):
        return '''
                        _.-..
                      ,'9 )\)`-.,.--.
                      `-.|           `.
                         \,      ,    \)
                          `.  )._\   (\\
                            |//   `-,//
                            ]||    //"
                            ""    ""

                      __
            ,'```--''¨  ``-''-.
          ,'            ,-- ,-'.
         (//            `"'| 'a \\
           |    `;         |--._/
           \    _;-._,    /
            \__/\\\\   \__,'
             ||  `'   \|\\\\
             \\\\        \\\\`'
              `'        `'
'''