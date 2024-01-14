import React, { useState } from "react";
import axios from "axios";
import { Typography, Box, Button, TextField } from "@mui/material";


function Chat({ answer }) {
  const [content, setContent] = useState("");
  const chatApi= process.env.REACT_APP_CHAT_API;
  const handleChatClick = async () => {
    try {
      const uploadResponse = await axios.post(
        chatApi,
        {
          user_message: content,
        },
        {
          headers: {
            "Content-Type": "application/json", 
          },
        }
      );
      console.log("Message sent successfully:", uploadResponse.data);
      return uploadResponse.data;
    } catch (error) {
      console.error("Failed to send message!", error);
    }
  };

  return (
    <Box>
      <Box sx={{ p: 3, mt: "5vh" }}>
        <TextField
          value={content}
          defaultValue={answer}
          onChange={(e) => setContent(e.target.value)}
        />
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            marginTop: "10px",
          }}
        >
          <Button variant="contained" color="primary" onClick={handleChatClick}>
            Chat
          </Button>
        </div>
      </Box>
    </Box>
  );
}
export default Chat;