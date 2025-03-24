import { MCPTool } from "mcp-framework";
import { z } from "zod";

interface GetClockInput {

}

class GetClockTool extends MCPTool<GetClockInput> {
  name = "get_clock";
  description = "Get current time as ISO string";

  schema = {

  };

  async execute(input: GetClockInput) {
    const date = new Date(Date.now());
    return date.toISOString();
  }
}

export default GetClockTool;