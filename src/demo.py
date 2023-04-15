from transformers import BertTokenizer, GPT2LMHeadModel, TextGenerationPipeline

if __name__ == '__main__':

    tokenizer = BertTokenizer.from_pretrained('MOBAGPT/vocab.txt')
    model = GPT2LMHeadModel.from_pretrained('MOBAGPT')
    text = "事件名称 : 击杀情况对比；范围 : 全场；MVP类型 : 击杀人数最多的；MVP补充解释 : 击杀 敌方；具体次数 : 10；玩家 : 1；队伍 : 天辉；玩家名称 : Echo；英雄 : 虚无之灵；游戏时间 : 1634"
    text_generator = TextGenerationPipeline(model, tokenizer)
    res = text_generator(text, max_length=100, do_sample=True)
    print(res)


