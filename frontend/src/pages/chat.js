import React, { useState } from "react";
import axios from "axios";
import {
  Typography,
  Box,
  Button,
} from "@mui/material";
import { faCloudArrowDown } from "@fortawesome/free-solid-svg-icons";
import UploadButton from "../components/UploadButton";

function CreatePost() {
  const [postId, setPostId] = useState("");
  const [content, setContent] = useState("");
  const [file, setFile] = useState(null);

  const handleChatClick = async () => {
    try {
      const uploadResponse = await axios.post(
        `https://dea5-117-102-52-3.ngrok-free.app/chat`,
        {
          user_message: content,
        },
        {
          headers: {
            "Content-Type": "application/json", // Set content type for the FormData
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
export default CreatePost;
