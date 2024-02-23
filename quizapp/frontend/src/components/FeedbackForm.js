import React, { useState, useRef } from "react";
import axios from "axios";
import { Link, useNavigate } from "react-router-dom";

const FeedbackForm = () => {
  const navigate = useNavigate();
  const handleSubmit = (e) => {
    e.preventDefault();

    navigate("/thankyou");
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
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
