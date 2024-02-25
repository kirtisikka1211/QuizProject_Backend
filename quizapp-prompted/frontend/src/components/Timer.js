import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const useTimer = () => {
  const navigate = useNavigate();
  const [timeLeft, setTimeLeft] = useState(5400); 

  useEffect(() => {
    if (timeLeft <= 0) navigate("/thankyou");
    const timeout = setTimeout(() => {
      setTimeLeft(timeLeft - 1);
    }, 1000);
    return () => clearTimeout(timeout);
  }, [timeLeft]);


  const hours = Math.floor(timeLeft / 3600);
  const remainingSeconds = timeLeft % 3600;
  const minutes = Math.floor(remainingSeconds / 60);
  const seconds = remainingSeconds % 60;
  const formattedTime = `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;

  return formattedTime;
};

export default useTimer;
