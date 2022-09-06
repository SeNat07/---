require: slotfilling/slotFilling.sc
  module = sys.zb-common
theme: /

    state: Start
        q!: $regex</start>
        a: Начнём.

    state: Hello
        q!: *(привет*/здравствуй*/добр*)*
        a: Привет, я чат-бот Наташи
        go!: /WhatsUp
        
    state: WhatsUp
        a: Как дела?  
        
        state: Great
            q: *(отлично/супер/замечательно/великолепно)*
            a: Я рад за Вас, у хорошего человека дела плохи не бывают!
        
        state: Good
            q: *(хорош*/норм*)*
            a: Я рад за Вас, все лучшее - впереди!
        
        state: Bad
            q: *(плох*/не(очень/хорош*))*
            a: Не стоит из-за этого грустить. Терпения Вам!    

    state: HowAreYou
        q!: *(как (ты/твои*))*
        a: Все замечательно!
        go: /Joke
    
    state: Joke || modal = true
        a: Хочешь, расскажу шутку?
        buttons:
            "Да" -> ./JokeYes
            "Нет" -> ./JokeNo
        
        state: ClickButtons
            q: *
            a: Нажмите, пожалуйста, кнопку.
            #go!: ..
            
        state: JokeNo
        a: Ну хорошо, расскажу, когда у тебя будет настроение.
        
        state: JokeYes
        a: Лови шутку:
        #go: /JokeText 
        
            #state: JokeText
                #random:
                   # a: Пора бы перестать строить планы на прошлое.
                    #a: Утро всегда доброе, а дальше сами.
                    #a: Взятка унижает человека. Особенно маленькая.
                    #a: Существует два мнения: одно мое, другое глупое.
                    #a: Некоторые весьма искренне думают, что они думают.
                    #a: Скорость моего интернета научила меня терпению.
            
                #state: JokeContinue
                    #q: *(еще/ещё/давай еще/хочу еще)*
                    #a: Ну хорошо, расскажу, когда у тебя будет настроение.  
                    #go!: /JokeText
        
        
    state: Bye
        intent!: /пока
        a: Пока, мой милый друг. Возвращайся!

    state: NoMatch
        event!: noMatch || noContext=true
        a: Я не понял. Вы сказали: {{$request.query}}

    state: Match
        event!: match
        a: {{$context.intent.answer}}