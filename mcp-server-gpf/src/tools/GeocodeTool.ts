import { MCPTool } from "mcp-framework";
import { z } from "zod";

interface GeocodeInput {
  text: string;
}

class GeocodeTool extends MCPTool<GeocodeInput> {
  name = "geocode";
  description = "Géocodage d'un lieu à l'aide du service d'autocomplétion de la GéoPF";

  schema = {
    text: {
      type: z.string(),
      description: "Le texte devant être completé et géocodé",
    },
  };

  async execute(input: GeocodeInput) {
    const url = 'https://data.geopf.fr/geocodage/completion/?' + new URLSearchParams({
      text: input.text
    }).toString();

    // fetch and parse json
    const res = await fetch(url);
    return await res.json();
  }
}

export default GeocodeTool;