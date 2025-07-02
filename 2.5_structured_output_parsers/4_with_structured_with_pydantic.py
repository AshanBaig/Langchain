# not woking OPEN AI ME CHLTA HY Ye sahi se
# typed dict ko pydantic me krain gye 
from typing import TypedDict,Annotated,Optional,Literal
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
    )

model = ChatHuggingFace(llm=llm)



class Reviews(BaseModel):
    # neche wle varibles pyantic me defin krte hain ab
    key_theme : list[str] =  Field(description="write down all key themes disscussed in the review in a list",default=None)
    summary : str = Field(description="A breif summary f the review ",)
    sentiments : Literal["pos","neg"] = Field(description="Return sentimnt of the review either negative postive or moderate")
    pros : Optional[str] = Field(default=None,description="write down all pros disscussed in the review in a list")
    cons : Optional[str] = Field(default=None,description="write down all cons disscussed in the review in a list")
    name : Optional[str] = Field(default="Unknown",description="person name who give review dont mentiond name by urs")
     
    
    
    
    
    # key_theme: Annotated[list[str],"write down all key themes disscussed in the review in a list"]
    # summary: Annotated[str,"A breif summary f the review "]   
    # sentiments:Annotated[str,"Return sentimnt of the review either negative postive or moderate"]
    # pros: Annotated[Optional[list[str]],"write down all pros disscussed in the review in a list"]
    # cons: Annotated[Optional[list[str]],"write down all cons disscussed in the review in a list"]
    # name:Annotated[Optional[str],"person name who give review dont mentiond name by urs"]



structured_model = model.with_structured_output(Reviews)
# model ko invoke ke bjae structured_model ko kro
rev1="I bought this a few weeks ago and so far it's been working really well. The quality feels solid and it looks exactly like the pictures. Setup was easy and quick. I’ve used it daily and haven’t had any issues. Definitely worth the money. Would recommend to others."
rev2= """I ordered this product thinking it would solve my daily issues, and in some ways, it did. The packaging was neat, and the first impression was honestly better than expected. Build quality looks premium,
        though I'm not entirely sure how long it will last. It performs well on basic tasks, but occasionally it lags or behaves unexpectedly.
        Maybe it's just my usage style, or maybe a firmware update is needed. 
        The instructions weren’t super clear, so I had to figure out some parts on my own.
        Customer support replied once and then never followed up, which is odd. It's hard to say whether I love it or just tolerate it.

        Pros: Nice design, decent performance, feels good to use.
        Cons: Inconsistent behavior, vague manual, average support."""
        
rev3 = """At first, I wasn’t sure what to expect, but when it arrived, it looked really sleek and modern.
        It worked fine on the first day, then started making a weird noise—though it still works.
        Sometimes it performs like a premium product, other times it just feels average. 
        The buttons are smooth, but the interface is a little tricky to understand. 
        I thought it was plug-and-play, but ended up watching two tutorials. Build quality seems strong, 
        but I’m scared to drop it. It connects well to my phone but randomly disconnects once in a while.
        Not sure if it’s a setting I messed up or the product itself. 
        It’s one of those things you want to like fully, but something always holds you back.
        Maybe it just needs a little more time to impress me."""

rev4="Product is quite good"
# result = structured_model.invoke(rev4)
# print(result) # dict a rhi hy # nanme nhi ayga bcz mentiion nhu hy mere pas a rha bcz i am using sasta AI
