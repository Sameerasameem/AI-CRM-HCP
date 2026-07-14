import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { setReply } from "./store";
import "./App.css";

function App() {
  const dispatch = useDispatch();
  const reply = useSelector((state) => state.crm.reply);

  const [form, setForm] = useState({
    doctor: "",
    hospital: "",
    date: "",
    notes: "",
  });

  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const saveInteraction = async () => {
    const text = `Log my meeting with ${form.doctor} from ${form.hospital} on ${form.date}, ${form.notes}`;

    const response = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message: text,
      }),
    });

    const data = await response.json();

    dispatch(setReply(data.reply));
    alert(data.reply);
  };

  const sendMessage = async () => {
    const response = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message,
      }),
    });

    const data = await response.json();

    dispatch(setReply(data.reply));
  };

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h1>AI CRM - Log Interaction</h1>

      <h3>HCP Interaction Form</h3>

      <input
        type="text"
        name="doctor"
        placeholder="Doctor Name"
        value={form.doctor}
        onChange={handleChange}
      />

      <br />
      <br />

      <input
        type="text"
        name="hospital"
        placeholder="Hospital"
        value={form.hospital}
        onChange={handleChange}
      />

      <br />
      <br />

      <input
        type="date"
        name="date"
        value={form.date}
        onChange={handleChange}
      />

      <br />
      <br />

      <textarea
        name="notes"
        placeholder="Interaction Notes"
        rows="5"
        cols="40"
        value={form.notes}
        onChange={handleChange}
      />

      <br />
      <br />

      <button onClick={saveInteraction}>
        Save Interaction
      </button>

      <hr />

      <h3>AI Chat</h3>

      <textarea
        rows="4"
        cols="50"
        placeholder="Type your message..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <br />
      <br />

      <button onClick={sendMessage}>
        Send
      </button>

      <h3>AI Response</h3>

      <div
        style={{
          border: "1px solid gray",
          padding: "10px",
          minHeight: "80px",
        }}
      >
        {reply}
      </div>
    </div>
  );
}

export default App;