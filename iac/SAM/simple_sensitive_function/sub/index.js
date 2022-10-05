exports.handler1 = async (event) => {
    eval(event.body); // Noncompliant (S5334)
    eval(event.headers["User-Agent"]); // Noncompliant (S5334)
    eval(event.queryStringParameters); // Noncompliant (S5334)
    eval(event.pathParameters); // Noncompliant (S5334)
    eval(event.requestContext.identity.userAgent); // Noncompliant (S5334)
  };
  
  exports.handler2 = async (event) => {
    eval(event.body); // Noncompliant (S5334)
  };
  
  exports.handler3 = async (event) => {
    eval(event.body); // Ok
  };