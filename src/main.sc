require: slotfilling/slotFilling.sc
  module = sys.zb-common
theme: /

    state: Start
        q!: $regex</start>
        a: Начнём.

    state: Hello
        intent!: /привет
        a: Привет, я чат-бот Наташи
        go!: /WhatsUp
        
    state: WhatsUp
        a: Как дела?  
        
        state: Great
            q!: /отлично
            a: Я рад за Вас, у хорошего человека дела плохи не бывают!
        
        state: Good
            q!: /хорошо
            a: Я рад за Вас, все лучшее - впереди!
        
        state: Bad
            q!: /плохо
            a: Не стоит из-за этого грустить. Терпения Вам!    

    state: /WhatsUp2
        q!: /Как дела?
        a: Все замечательно! Когда нечем думать, проблем не возникает.
        
    state: Bye
        intent!: /пока
        a: Пока, мой милый друг. Возвращайся!

    state: NoMatch
        event!: noMatch
        a: Я не понял. Вы сказали: {{$request.query}}

    state: Match
        event!: match
        a: {{$context.intent.answer}}