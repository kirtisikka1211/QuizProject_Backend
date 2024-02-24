import React, { useState, useRef } from "react";
import axios from "axios";
import { Link, useNavigate } from "react-router-dom";

const BorderForm = () => {
  const navigate = useNavigate();
  const windowWidth = useRef(window.innerWidth);
  const windowHeight = useRef(window.innerHeight);
  const [formData, setFormData] = useState({
    roll_no: "",
    name: "",
    email: "",
    gender:"",
    age:"",
    degree:"",
    uni:"",
    cgpa:"",
    device_dimensions:"",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  formData.device_dimensions=`${windowWidth.current},${windowHeight.current}`;

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post("https://hci-analysis.software/api/users/", formData)
      .then((response) => {})
      .catch((error) => {
        console.error("Error while making the Axios request:", error);
      });

    navigate(`/Welcome?roll_no=${formData.roll_no}`);
  };

  return (
    <div className="flex justify-center items-center h-screen px-5 bg-gradient-to-b from-blue-texts to-white">
      <form
        onSubmit={handleSubmit}
        className="max-w-md mx-auto sm:h-30 h-5/6 border border-blue-texts p-6 rounded-lg bg-white md:w-1/2 overflow-y-auto"
      >
        <div className="flex justify-center items-center mb-10 text-3xl text-blue-texts">
          Welcome
        </div>
        <div className="flex justify-center items-center mb-10 text-xl text-blue-texts">
          Please enter the following details before getting started
        </div>
        <div className="mb-7">
          <label
            htmlFor="name"
            className="block mb-2 text-sm font-medium text-blue-texts"
          >
            Name
          </label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            className="border border-blue-texts p-2.5 rounded-md w-full"
            placeholder="enter your name"
            required
          />
        </div>
        <div className="mb-7">
          <label
            htmlFor="roll_no"
            className="block mb-2 text-sm font-medium text-blue-texts"
          >
            Roll Number
          </label>
          <input
            type="text"
            id="roll_no"
            name="roll_no"
            value={formData.roll_no}
            onChange={handleChange}
            className="border border-blue-texts p-2.5 rounded-md w-full"
            placeholder="enter your roll number"
            required
          />
        </div>
        <div className="mb-7">
          <label
            htmlFor="email"
            className="block mb-2 text-sm font-medium text-blue-texts"
          >
            Email
          </label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            className="border border-blue-texts p-2.5 rounded-md w-full max-w-md" 
            placeholder="am.en.u4cse22001@am.students.amrita.edu"
            required
          />
        </div>
        <div className="mb-7">
          <label
            htmlFor="gender"
            className="block mb-2 text-sm font-medium text-blue-texts"
          >
            Gender
          </label>
          <input
            type="text"
            id="gender"
            name="gender"
            value={formData.gender}
            onChange={handleChange}
            className="border border-blue-texts p-2.5 rounded-md w-full"
            placeholder="enter your gender"
            required
          />
        </div>
        <div className="mb-7">
          <label
            htmlFor="age"
            className="block mb-2 text-sm font-medium text-blue-texts"
          >
            Age
          </label>
          <input
            type="text"
            id="age"
            name="age"
            value={formData.age}
            onChange={handleChange}
            className="border border-blue-texts p-2.5 rounded-md w-full"
            placeholder="enter your age"
            required
          />
        </div>
        <div className="mb-7">
          <label
            htmlFor="degree"
            className="block mb-2 text-sm font-medium text-blue-texts"
          >
            Degree
          </label>
          <input
            type="text"
            id="degree"
            name="degree"
            value={formData.degree}
            onChange={handleChange}
            className="border border-blue-texts p-2.5 rounded-md w-full"
            placeholder="enter your degree"
            required
          />
        </div>
        <div className="mb-7">
          <label
            htmlFor="uni"
            className="block mb-2 text-sm font-medium text-blue-texts"
          >
            University
          </label>
          <input
            type="text"
            id="uni"
            name="uni"
            value={formData.uni}
            onChange={handleChange}
            className="border border-blue-texts p-2.5 rounded-md w-full"
            placeholder="enter your University"
            required
          />
        </div>
        <div className="mb-20">
          <label
            htmlFor="cgpa"
            className="block mb-2 text-sm font-medium text-blue-texts"
          >
            cgpa
          </label>
          <input
            type="text"
            id="cgpa"
            name="cgpa"
            value={formData.cgpa}
            onChange={handleChange}
            className="border border-blue-texts p-2.5 rounded-md w-full"
            placeholder="enter your cgpa"
            required
          />
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

export default BorderForm;
