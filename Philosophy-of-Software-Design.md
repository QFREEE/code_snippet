
### Chapter 2:The Nature of Complexity
#### Complexity shows itself in 3 ways: 
1. Change amplification - small changes requires code changes in many different places.
2. Cognitive load - how much a developer needs to know in order to complete a task. Less lins of code doesn't equate to less cognititve load.
3. Unknown unknow -  it is unclear what to do or whether a proposed solution will even work.

#### Causes of complexity 
1. dependencies - make dependencies as simple and obvious as possible 
2. obscurity - The best way to reduce obscurity is by simplifying the system design.

Complexity comes from an accumulation of dependencies and obscurities. As complexity increases, it leads to change amplification, a high cognitive load, and unknown unknowns. 

### Chapter 3:Working Code Isn’t Enough

##### tacical programming
- tacical programming to get something working quickly-> introduce bad system design 
- Once you start down the tactical path, it’s difficult to change.
-  recognize tactical tornado at work

##### strategic programming 
- long term structure of the system. **to facilitate those future extensions**
- strategic programming is an investment mindset. 
- find simple design, write good docs, fix design program and small improvement to system design

### Chapter 4: Modules should be deep
##### modular design 
- The goal of modular design is to minimize the dependencies between modules.
- The best modules are those whose interfaces are much simpler than their implementations.

##### interface
- formal and informal info 
- One of the benefits of a clearly specified interface is that it indicates exactly what developers need to know in order to use the associated module. 
##### abstractions 
- First, it can include details that are not really **important**; when this happens, it makes the abstraction more complicated than necessary, which increases the cognitive load on developers using the abstraction. The second error is when an abstraction omits details that really are **important**. This results in obscurity: developers looking only at the abstraction will not have all the information they need to use the abstraction correctly

##### deep modules
powerful functionality with simple interfaces
- Unix I/O
- garbage collector 

Classitis may result in classes that are individually simple, but it increases the complexity of the overall system.
