import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const FeedbackForm = () => {
  const navigate = useNavigate();
  const [questions, setQuestions] = useState([]);
  const [selectedOptions, setSelectedOptions] = useState({});
  const [questionCounter, setQuestionCounter] = useState(1);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("https://hci-analysis.software/api/feedback/");
        if (
          response.data &&
          Array.isArray(response.data) &&
          response.data.length > 0
        ) {
          setQuestions(response.data);
          const initialSelectedOptions = {};
          response.data.forEach(question => {
            initialSelectedOptions[question.id] = null;
          });
          setSelectedOptions(initialSelectedOptions);
        } else {
          console.error("No questions found.");
        }
      } catch (error) {
        console.error("Error fetching questions:", error);
      }
    };
    fetchData();
  }, []);

  const handleOptionSelect = (questionId, option) => {
    setSelectedOptions(prevState => ({
      ...prevState,
      [questionId]: option
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    navigate("/thankyou");
  };

  return (
    <div className="flex justify-center items-center h-screen px-5 bg-gradient-to-b from-blue-texts to-white">
      <form
        onSubmit={handleSubmit}
        className="max-w-md mx-auto sm:h-30 h-5/6 border border-blue-texts p-6 rounded-lg bg-white md:w-1/2 overflow-y-auto"
      >
        <div className="flex flex-col p-4 space-y-7 ">
          {questions.map((question, index) => (
            <div key={question.id}>
              <p>Q.{questionCounter + index}. {question.questions}</p>
              <div className="space-y-2">
                {['option1', 'option2', 'option3', 'option4', 'option5'].map((optionKey) => (
                  <div key={optionKey} className="flex items-center">
                    <input
                      type="radio"
                      value={question[optionKey]}
                      checked={selectedOptions[question.id] === question[optionKey]}
                      onChange={() => handleOptionSelect(question.id, question[optionKey])}
                      className="mr-2"
                    />
                    <label>{question[optionKey]}</label>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
        <button
          type="submit"
          className="text-white mb-10 bg-blue-texts hover:bg-[#4999c4] focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-md text-sm w-full py-2.5 text-center"
        >
          Submit
        </button>
      </form>
    </div>
  );
};

export default FeedbackForm;
