# user s 1 document le kr  uske note s bhi bane gye or 1 quiz bhi generate krain gye us se realted or end me dono ko merge kr de gye

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser  # str means direct string ayegi .content kr ke nhi nikalna prga
from langchain.schema.runnable import RunnableParallel
GROQ_API_KEY = "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"

model1 = ChatOpenAI(
    api_key = GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",  # Groq OpenAI-compatible endpoint
    model="llama3-8b-8192"
)
prompt1 = PromptTemplate(
    template="Genrate short and simple notes from the following text \n {text}",
    input_variables=["text"]
)
prompt2 = PromptTemplate(
    template="Generate 5 shorts questions anwer from the following text \n  {text}",
    input_variables=["text"]
)
prompt3 = PromptTemplate(
    template = "Merge the provided notes and quiz into a single document \n notes ->{notes} and quiz -> {quiz}",
    input_variables=["notes","quiz"]
)
parser = StrOutputParser()

# chain 2 part me develpo kraingye parallel wli alag series wli alga


parallel_chain = RunnableParallel(
    {"notes":prompt1|model1|parser,
     "quiz": prompt2 | model1 | parser
     }
)

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """In linear regression, the relationships are modeled using linear predictor functions whose unknown model parameters are estimated from the data. Most commonly, the conditional mean of the response given the values of the explanatory variables (or predictors) is assumed to be an affine function of those values; less commonly, the conditional median or some other quantile is used. Like all forms of regression analysis, linear regression focuses on the conditional probability distribution of the response given the values of the predictors, rather than on the joint probability distribution of all of these variables, which is the domain of multivariate analysis.

Linear regression is also a type of machine learning algorithm, more specifically a supervised algorithm, that learns from the labelled datasets and maps the data points to the most optimized linear functions that can be used for prediction on new datasets.[3]

Linear regression was the first type of regression analysis to be studied rigorously, and to be used extensively in practical applications.[4] This is because models which depend linearly on their unknown parameters are easier to fit than models which are non-linearly related to their parameters and because the statistical properties of the resulting estimators are easier to determine.

Linear regression has many practical uses. Most applications fall into one of the following two broad categories:

If the goal is error i.e. variance reduction in prediction or forecasting, linear regression can be used to fit a predictive model to an observed data set of values of the response and explanatory variables. After developing such a model, if additional values of the explanatory variables are collected without an accompanying response value, the fitted model can be used to make a prediction of the response.
If the goal is to explain variation in the response variable that can be attributed to variation in the explanatory variables, linear regression analysis can be applied to quantify the strength of the relationship between the response and the explanatory variables, and in particular to determine whether some explanatory variables may have no linear relationship with the response at all, or to identify which subsets of explanatory variables may contain redundant information about the response.
Linear regression models are often fitted using the least squares approach, but they may also be fitted in other ways, such as by minimizing the "lack of fit" in some other norm (as with least absolute deviations regression), or by minimizing a penalized version of the least squares cost function as in ridge regression (L2-norm penalty) and lasso (L1-norm penalty). Use of the Mean Squared Error (MSE) as the cost on a dataset that has many large outliers, can result in a model that fits the outliers more than the true data due to the higher importance assigned by MSE to large errors. So, cost functions that are robust to outliers should be used if the dataset has many large outliers. Conversely, the least squares approach can be used to fit models that are not linear models. Thus, although the terms "least squares" and "linear model" are closely linked, they are not synonymous.

"""


result =  chain.invoke({"text":text})
print(result)

print(chain.get_graph().print_ascii())