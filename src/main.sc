require: slotfilling/slotFilling.sc
  module = sys.zb-common
theme: / 

    state: Start
        q!: $regex</start>
        a: Начнём.

    state: Hello
        intent!: /Приветствие
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
        intent!: /KnowledgeBase/FAQ.Пустой шаблон FAQ/Root/Как дела
        a: Все замечательно!
        go!: /Joke

    state: Joke || modal = true
        q!: *(как дела/как ты/как твои дела)*
        a: Хочешь, расскажу шутку? || htmlEnabled = false
        buttons:
            "Да" -> /Joke/JokeYes
            "Нет" -> /Joke/JokeNo
            
        state: ClickButtons || noContext = true
            q: * || fromState = "/Joke", onlyThisState = false
            a: Нажмите, пожалуйста, кнопку.
            go!: /Joke
        
        state: JokeNo
            a: Ну хорошо, расскажу, когда у тебя будет настроение. || htmlEnabled = false, html = "Ну хорошо, расскажу, когда у тебя будет настроение."
            go!: /Continue
        
        state: JokeYes
            a: Лови шутку: || htmlEnabled = false, html = "Лови шутку:"
            go!: /Joke/JokeYes/JokeText

            state: JokeText
                random: 
                    a: Пора бы перестать строить планы на прошлое.
                    a: Утро всегда доброе, а дальше сами.
                    a: Взятка унижает человека. Особенно маленькая.
                    a: Существует два мнения: одно мое, другое глупое.
                    a: Некоторые весьма искренне думают, что они думают.
                    a: Скорость моего интернета научила меня терпению.
                go!: /Joke

    state: Continue
        a: Жду, пока ты со мной вновь заговоришь...
        
    state: Bye
        intent!: /Прощание
        a: Пока, мой милый друг. Возвращайся!

    state: NoMatch
        event!: noMatch || noContext=true
        a: Я не понял. Вы сказали: {{$request.query}}

    state: Match
        event!: match
        a: {{$context.intent.answer}}