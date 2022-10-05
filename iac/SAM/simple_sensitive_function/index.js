exports.handler = async (event) => {
    eval(event.body); // Noncompliant (S5334)
};